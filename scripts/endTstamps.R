data_18lun$end_tstamps <- lapply(strsplit(as.character(data_18lun$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_19mar$end_tstamps <- lapply(strsplit(as.character(data_19mar$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_20mie$end_tstamps <- lapply(strsplit(as.character(data_20mie$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_21jue$end_tstamps <- lapply(strsplit(as.character(data_21jue$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_22vie$end_tstamps <- lapply(strsplit(as.character(data_22vie$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_23sab$end_tstamps <- lapply(strsplit(as.character(data_23sab$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_24dom$end_tstamps <- lapply(strsplit(as.character(data_24dom$end_tstamps), ";"), function(x) sort(as.numeric(x)))

tstamps_18lun <- lapply(data_18lun$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01")
tstamps_19mar <- lapply(data_19mar$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01")
tstamps_20mie <- lapply(data_20mie$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01")
tstamps_21jue <- lapply(data_21jue$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01")
tstamps_22vie <- lapply(data_22vie$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01")
tstamps_23sab <- lapply(data_23sab$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01")
tstamps_24dom <- lapply(data_24dom$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01")

for (i in 1:10) {
    hist(tstamps_18lun[[i]], breaks="hours", main=sprintf("conexión %s, L18may",i), freq=T)
}
for (i in 1:10) {
    hist(tstamps_19mar[[i]], breaks="hours", main=sprintf("conexión %s, M19may",i), freq=T)
}
for (i in 1:10) {
    hist(tstamps_20mie[[i]], breaks="hours", main=sprintf("conexión %s, X20may",i), freq=T)
}
for (i in 1:10) {
    hist(tstamps_21jue[[i]], breaks="hours", main=sprintf("conexión %s, J21may",i), freq=T)
}
for (i in 1:10) {
    hist(tstamps_22vie[[i]], breaks="hours", main=sprintf("conexión %s, V22may",i), freq=T)
}
for (i in 1:10) {
    hist(tstamps_23sab[[i]], breaks="hours", main=sprintf("conexión %s, S23may",i), freq=T)
}
for (i in 1:10) {
    hist(tstamps_24dom[[i]], breaks="hours", main=sprintf("conexión %s, D24may",i), freq=T)
}

#colrs = c("#4E79A780", "#F28E2B80", "#E1575980", "#76B7B280", "#59A14F80", "#EDC94880", "#B07AA180", "#FF9DA780", "#9C755F80", "#BAB0AC80")
