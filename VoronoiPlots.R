library(deldir)
library(zoom)
library(ggplot2)

df <- equilibratedData

#This creates the voronoi line segments
voronoi <- deldir(df$x, df$y)

#Now we can make a plot
ggplot(data=df, aes(x=x,y=y)) +
  #Plot the voronoi lines
  geom_segment(
    aes(x = x1, y = y1, xend = x2, yend = y2),
    size = 1,
    data = voronoi$dirsgs,
    linetype = 1,
    color= "#FFB958") + 
  #Plot the points
  geom_point(
    fill=rgb(70,130,180,255,maxColorValue=255),
    pch='.',
    size = 2,
    col=df$Labels+1)
zm()