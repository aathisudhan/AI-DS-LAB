x <- 1:10
y <- c(2, 5, 7, 8, 9, 12, 14, 18, 20, 24)  # numeric values
categories <- c("A", "B", "C", "D")
values <- c(25, 15, 35, 25)                # for pie & bar chart

plot(x, y,
     type = "o",              # 'o' for line + points
     col = "blue",            # line color
     lwd = 2,                 # line width
     main = "Line Plot Example",
     xlab = "X Values",
     ylab = "Y Values",
     pch = 16)                # solid circle points

plot(x, y,
     type = "p",              # 'p' for points only
     col = "red",
     main = "Scatter Plot Example",
     xlab = "X Values",
     ylab = "Y Values",
     pch = 19)                # filled circles

pie(values,
    labels = categories,
    col = rainbow(length(values)),
    main = "Pie Chart Example")

barplot(values,
        names.arg = categories,
        col = c("skyblue", "orange", "pink", "green"),
        main = "Bar Chart Example",
        xlab = "Categories",
        ylab = "Values")
