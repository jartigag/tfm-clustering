# Antes de ajustar a Anova, debemos verificar que los datos cumplan con ciertos requisitos, o assumptions:
# 1. Los datos deben ajustarse a la distribución normal: tapply(datos,grupo,shapiro.test)
# 2. Debe existir homogeneidad en las varianzas: library(car); leveneTest(datos~grupo)
# (https://rstudio-pubs-static.s3.amazonaws.com/283855_ce36f74b351b43659cc171c576931b02.html)

            # var. depend.     ~  var. independ.
anova <- aov(data_18lun$dst_port ~ data_18lun$dst_ip)

summary(anova)
#                    Df Sum Sq Mean Sq F value   Pr(>F)
#data_18lun$dst_ip    1     69   68.62   26.15 3.28e-07 ***
#Residuals         4811  12624    2.62
#---
#Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# efecto significativo de la variable dst_ip (p-valor menor que 0.01)

plot(anova) # devuelve 4 gráficas de dispersión:
#           - residuals vs fitted values
#           - "Normal Q-Q": standarized residuals vs theoretical quantiles
#           - "Scale-Location": sqrt(standarized residuals) vs fitted values
#           - standarized residuals vs leverage

# Otros ejemplos:
# calcular media por condición:
# > tapply(ej1$Vigilancia,ej1$Dosis,mean)
# a b c
# 32.50 28.25 19.25
