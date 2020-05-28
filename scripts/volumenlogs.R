raw       <-     c( 47990233167,  49187772177,  49668247110,  52672266521,  49253115426,  43913255316, 46270619052);
extracted <-     c(  5766385969,   5939145359,   5883398905,   6116088410,   5739938280,   4961969981, 5219956643);
dates <- as.Date(c("18-05-2020", "19-05-2020", "20-05-2020", "21-05-2020", "22-05-2020", "23-05-2020", "24-05-2020"), "%d-%m-%y");
plot(dates, raw/10^9, type="l", lty=2, ylab="Volumen de datos (GB)", xlab="Fecha (en mayo de 2020)", xaxt="n", ylim=range(c(raw, extracted)/10^9), main="Procesado de los logs del firewall Fortinet");
lines(dates, extracted/10^9, type="l", col="blue");
axis(1, dates, format(dates, "%a %d"));
legend("right",lty=c(2,1), col=c("black","blue"), bty="n", legend=c("En bruto", "Resultado de la extracción"))
