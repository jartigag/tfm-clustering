# $, like everything else in R, is a function. https://stackoverflow.com/a/18228613

plot(ecdf(data_18lun[$dst_ip]), col="lightgrey", verticals = TRUE, main = "count(dst_ip)", sub = "Semana L18 a D24 mayo 2020")
lines(ecdf(data_19mar[$dst_ip]), col="lightgrey", verticals = TRUE)
lines(ecdf(data_20mie[$dst_ip]), col="lightgrey", verticals = TRUE)
lines(ecdf(data_21jue[$dst_ip]), col="lightgrey", verticals = TRUE)
lines(ecdf(data_22vie[$dst_ip]), col="lightgrey", verticals = TRUE)
lines(ecdf(data_23sab[$dst_ip]), col="grey", verticals = TRUE)
lines(ecdf(data_24dom[$dst_ip]), col="grey", verticals = TRUE)

plot(ecdf(data_18lun[$dst_port]), col="lightgrey", verticals = TRUE, main = "count(dst_port)", sub = "Semana L18 a D24 mayo 2020")
lines(ecdf(data_19mar[$dst_port]), col="lightgrey", verticals = TRUE)
lines(ecdf(data_20mie[$dst_port]), col="lightgrey", verticals = TRUE)
lines(ecdf(data_21jue[$dst_port]), col="lightgrey", verticals = TRUE)
lines(ecdf(data_22vie[$dst_port]), col="lightgrey", verticals = TRUE)
lines(ecdf(data_23sab[$dst_port]), col="grey", verticals = TRUE)
lines(ecdf(data_24dom[$dst_port]), col="grey", verticals = TRUE)

plot(ecdf(data_18lun$count_events), col="lightgrey", verticals = TRUE, main = "count(events)", sub = "Semana L18 a D24 mayo 2020", log="x")
lines(ecdf(data_19mar$count_events), col="lightgrey", verticals = TRUE)
lines(ecdf(data_20mie$count_events), col="lightgrey", verticals = TRUE)
lines(ecdf(data_21jue$count_events), col="lightgrey", verticals = TRUE)
lines(ecdf(data_22vie$count_events), col="lightgrey", verticals = TRUE)
lines(ecdf(data_23sab$count_events), col="grey", verticals = TRUE)
lines(ecdf(data_24dom$count_events), col="grey", verticals = TRUE)

# Save Plot as PDF:
#   PDF Size: 7.00x7.00 inches
