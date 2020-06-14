# > start.time <- Sys.time()
# > source("g/tfm/scripts/endTstamps.R")
# > end.time <- Sys.time()
# > time.taken <- end.time - start.time
# > time.taken
# Time difference of 26.83222 secs

data_18lun$end_tstamps <- lapply(strsplit(as.character(data_18lun$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_19mar$end_tstamps <- lapply(strsplit(as.character(data_19mar$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_20mie$end_tstamps <- lapply(strsplit(as.character(data_20mie$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_21jue$end_tstamps <- lapply(strsplit(as.character(data_21jue$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_22vie$end_tstamps <- lapply(strsplit(as.character(data_22vie$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_23sab$end_tstamps <- lapply(strsplit(as.character(data_23sab$end_tstamps), ";"), function(x) sort(as.numeric(x)))
data_24dom$end_tstamps <- lapply(strsplit(as.character(data_24dom$end_tstamps), ";"), function(x) sort(as.numeric(x)))

tstamps_18lun <- lapply(data_18lun$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01"))
tstamps_19mar <- lapply(data_19mar$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01"))
tstamps_20mie <- lapply(data_20mie$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01"))
tstamps_21jue <- lapply(data_21jue$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01"))
tstamps_22vie <- lapply(data_22vie$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01"))
tstamps_23sab <- lapply(data_23sab$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01"))
tstamps_24dom <- lapply(data_24dom$end_tstamps, function(x) as.POSIXct(x, origin="1970-01-01"))

colrs = c("#4E79A780", "#F28E2B80", "#E1575980", "#76B7B280", "#59A14F80", "#EDC94880", "#B07AA180", "#FF9DA780", "#9C755F80", "#BAB0AC80")

hists = c()
# get max. freq. of all tstamps_18lun rows:
max = 0
for (i in 1:10) {
    hists[[i]] = hist(tstamps_18lun[[i]], breaks="hours", main=sprintf("conexión %s, L18may",i), freq=T, col=colrs[[i]]) #plot=F)
    if (max(hists[[i]]$counts)>max) max = max(hists[[i]]$counts)
}

# plot every hists together, with y-axis adjusted:
hist(tstamps_18lun[[1]], breaks="hours", main="10 conexiones del L18may", freq=T, lty="blank", col=colrs[[1]], ylim=range(0,max))
for (i in 2:10) {
    lines(hists[[i]], lty="blank", col=colrs[[i]])
}

###
# same for each day:
##

hists = c()
# get max. freq. of all tstamps_19mar rows:
max = 0
for (i in 1:10) {
    hists[[i]] = hist(tstamps_19mar[[i]], breaks="hours", main=sprintf("conexión %s, M19may",i), freq=T, col=colrs[[i]]) #plot=F)
    if (max(hists[[i]]$counts)>max) max = max(hists[[i]]$counts)
}

# plot every hists together, with y-axis adjusted:
hist(tstamps_19mar[[1]], breaks="hours", main="10 conexiones del M19may", freq=T, lty="blank", col=colrs[[1]], ylim=range(0,max))
for (i in 2:10) {
    lines(hists[[i]], lty="blank", col=colrs[[i]])
}

hists = c()
# get max. freq. of all tstamps_20mie rows:
max = 0
for (i in 1:10) {
    hists[[i]] = hist(tstamps_20mie[[i]], breaks="hours", main=sprintf("conexión %s, X20may",i), freq=T, col=colrs[[i]]) #plot=F)
    if (max(hists[[i]]$counts)>max) max = max(hists[[i]]$counts)
}

# plot every hists together, with y-axis adjusted:
hist(tstamps_20mie[[1]], breaks="hours", main="10 conexiones del X20may", freq=T, lty="blank", col=colrs[[1]], ylim=range(0,max))
for (i in 2:10) {
    lines(hists[[i]], lty="blank", col=colrs[[i]])
}

hists = c()
# get max. freq. of all tstamps_21jue rows:
max = 0
for (i in 1:10) {
    hists[[i]] = hist(tstamps_21jue[[i]], breaks="hours", main=sprintf("conexión %s, J21may",i), freq=T, col=colrs[[i]]) #plot=F)
    if (max(hists[[i]]$counts)>max) max = max(hists[[i]]$counts)
}

# plot every hists together, with y-axis adjusted:
hist(tstamps_21jue[[1]], breaks="hours", main="10 conexiones del J21may", freq=T, lty="blank", col=colrs[[1]], ylim=range(0,max))
for (i in 2:10) {
    lines(hists[[i]], lty="blank", col=colrs[[i]])
}

hists = c()
# get max. freq. of all tstamps_22vie rows:
max = 0
for (i in 1:10) {
    hists[[i]] = hist(tstamps_22vie[[i]], breaks="hours", main=sprintf("conexión %s, V22may",i), freq=T, col=colrs[[i]]) #plot=F)
    if (max(hists[[i]]$counts)>max) max = max(hists[[i]]$counts)
}

# plot every hists together, with y-axis adjusted:
hist(tstamps_22vie[[1]], breaks="hours", main="10 conexiones del V22may", freq=T, lty="blank", col=colrs[[1]], ylim=range(0,max))
for (i in 2:10) {
    lines(hists[[i]], lty="blank", col=colrs[[i]])
}

hists = c()
# get max. freq. of all tstamps_23sab rows:
max = 0
for (i in 1:10) {
    hists[[i]] = hist(tstamps_23sab[[i]], breaks="hours", main=sprintf("conexión %s, S23may",i), freq=T, col=colrs[[i]]) #plot=F)
    if (max(hists[[i]]$counts)>max) max = max(hists[[i]]$counts)
}

# plot every hists together, with y-axis adjusted:
hist(tstamps_23sab[[1]], breaks="hours", main="10 conexiones del S23may", freq=T, lty="blank", col=colrs[[1]], ylim=range(0,max))
for (i in 2:10) {
    lines(hists[[i]], lty="blank", col=colrs[[i]])
}

hists = c()
# get max. freq. of all tstamps_24dom rows:
max = 0
for (i in 1:10) {
    hists[[i]] = hist(tstamps_24dom[[i]], breaks="hours", main=sprintf("conexión %s, D24may",i), freq=T, col=colrs[[i]]) #plot=F)
    if (max(hists[[i]]$counts)>max) max = max(hists[[i]]$counts)
}

# plot every hists together, with y-axis adjusted:
hist(tstamps_24dom[[1]], breaks="hours", main="10 conexiones del D24may", freq=T, lty="blank", col=colrs[[1]], ylim=range(0,max))
for (i in 2:10) {
    lines(hists[[i]], lty="blank", col=colrs[[i]])
}
