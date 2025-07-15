# Step 1: Import Dataset
# Assuming the dataset is named "benchmark.csv" and located in your working directory
url <- "https://raw.githubusercontent.com/aathisudhan/AI-DS-LAB/main/DEV/SampleData2.csv"
data <- read.csv(url)

# Step 2: View Structure
str(data)

# Step 3: Summary Statistics
summary(data)

# Step 4: Preview First & Last Few Rows
head(data)
tail(data)

# Step 5: Check Missing Values
sum(is.na(data))          # Total missing values
colSums(is.na(data))      # Missing values column-wise

# Step 6: Descriptive Statistics
mean(data$Age)            # Mean Age
median(data$Age)          # Median Age

# Mode function (R does not have a built-in mode function)
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}
getmode(data$Age)         # Mode Age

range(data$Age)           # Min and Max
diff(range(data$Age))     # Range = Max - Min

var(data$Age)             # Variance of Age
sd(data$Age)              # Standard Deviation of Age

# Step 7: Quartiles
quantile(data$Age)        # 0%, 25%, 50%, 75%, 100%

# Step 8: Frequency Table for Categorical Variables
table(data$Gender)        # Frequency count
prop.table(table(data$Gender))  # Proportion

# Step 9: Visualization (Optional)
hist(data$Age, main="Histogram of Age", xlab="Age", col="skyblue", border="black")
boxplot(data$Income, main="Boxplot of Income", col="lightgreen", horizontal=TRUE)
barplot(table(data$MaritalStatus), main="Marital Status Distribution", col="orange")

