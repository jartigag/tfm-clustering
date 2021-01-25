df <- read.csv("~/g/tfm/scripts/results/2020-09-26-dataset.labeled.csv")
color_pallete_function <- colorRampPalette(c("red", "green", "blue", "yellow", "purple"))
palette <- color_pallete_function(nlevels(df$cluster))

# anom:
plot(x=df$count_events, y=df$avg_duration, xlab="count_events", ylab="avg_duration", pch=20, col=palette[df$cluster], xlim=range(0,500000))
legend(x="topright", legend=paste(levels(df$cluster)), col=palette, pch=19, cex=.8)

# udp:
plot(df$proto, col=palette[df$cluster], ylab="proto", xlab="instancia", pch=20)
legend(x="bottomright", legend=paste(levels(df$cluster)), col=palette, pch=19, cex=.8)

# long_duration:
plot(df$avg_duration, col=palette[df$cluster], ylab="avg_duration", xlab="instancia", pch=20, ylim=range(0,5000))
legend(x="topleft", legend=paste(levels(df$cluster)), col=palette, pch=19, cex=.8)

# many_cnxs/few_cnxs:
plot(df$dst_ip, col=palette[df$cluster], ylab="dst_ip", xlab="instancia", pch=20)
legend(x="topright", legend=paste(levels(df$cluster)), col=palette, pch=19, cex=.8)

# Export: {height=550, width=500}
