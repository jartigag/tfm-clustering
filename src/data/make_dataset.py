#!/usr/bin/env python3
#
#usage: ./src/data/make_dataset.py data/raw/ data/processed/

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import os
from src.features.build_features import process


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data (from data/raw) into
        cleaned data ready to be analyzed (saved in data/processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data..')

    def convert_bytes(num):
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    #for f in Path(input_filepath).iterdir():
    for f in Path(input_filepath).glob('*.log'):

        #TODO: extract tar.gz

        logger.info(f"({convert_bytes(f.stat().st_size)}) {f}")
        preprocess_command = f'''
        mawk -F"···" '{{OFS=","}}{{print $1,$2,$5"-"$6,$7,$9,$10,$11,$14,$15,$16,$17,$18}}' {f} \\
                > {Path(input_filepath).parent/'interim'/f.stem}.datavector.csv.log
        '''
        # f.stem is f.name without suffix
        logger.info(preprocess_command)
        os.system(preprocess_command)

        #TODO: logger.info(f"estimated RAM size needed: {x}")

        #./src/features/build_features.py data/interim/FORTINET_FIREWALL.2021-01-26T070500.featuresvector.csv > FORTINET_FIREWALL.2021-01-26T070500.aggmatrix.csv
        process_input =f"{Path(input_filepath).parent/'interim'/f.stem}.datavector.csv.log"
        process_output =f"{Path(input_filepath).parent/'processed'/f.stem}.aggmatrix.csv.log"
        logger = logging.getLogger(".".join([process.__module__,process.__name__]))
        process_command = f'''
        ./src/features/build_features.py {process_input} \\
                > {process_output}
        '''
        logger.info(process_command)
        process(process_input, output_file=process_output, time_slots=False)

    logger.info('final data set done.')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
