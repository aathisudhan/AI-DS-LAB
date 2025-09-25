# =========================
# Full BMI Analysis Project
# =========================

# Load required libraries
if(!require(ggplot2)) install.packages("ggplot2")
if(!require(dplyr)) install.packages("dplyr")
library(ggplot2)
library(dplyr)

# ---- Step 1: Collect multiple user inputs ----
cat("Welcome to the Full BMI Analysis Tool!\n")
cat("Enter number of users to analyze: ")
num_users <- as.numeric(readline())

# Initialize empty data frame
bmi_df <- data.frame(User = character(),
                     Weight = numeric(),
                     Height = numeric(),
                     BMI = numeric(),
                     Category = character(),
                     Suggestion = character(),
                     stringsAsFactors = FALSE)

# Loop to collect data for each user
for(i in 1:num_users){
  cat("\n--- User", i, "---\n")
  weight <- as.numeric(readline(prompt = "Enter weight in kg (e.g., 70): "))
  height <- as.numeric(readline(prompt = "Enter height in meters (e.g., 1.75): "))
  
  # Calculate BMI
  bmi <- round(weight / (height^2), 2)
  
  # Categorize BMI
  if(bmi < 18.5){
    category <- "Underweight"
  } else if(bmi >= 18.5 & bmi < 25){
    category <- "Normal weight"
  } else if(bmi >= 25 & bmi < 30){
    category <- "Overweight"
  } else{
    category <- "Obese"
  }
  
  # Add to dataframe
  bmi_df <- rbind(bmi_df, data.frame(User = paste("User", i),
                                     Weight = weight,
                                     Height = height,
                                     BMI = bmi,
                                     Category = category,
                                     Suggestion = suggestion,
                                     stringsAsFactors = FALSE))
}

# ---- Step 2: Display summary ----
cat("\n--- Summary Table ---\n")
print(bmi_df)

# ---- Step 3: Visualizations ----

# Pie chart for BMI categories
category_counts <- bmi_df %>%
  group_by(Category) %>%
  summarise(Count = n())

ggplot(category_counts, aes(x="", y=Count, fill=Category)) +
  geom_bar(stat="identity", width=1) +
  coord_polar("y") +
  geom_text(aes(label=paste0(Category, ": ", Count)), 
            position=position_stack(vjust=0.5)) +
  ggtitle("BMI Categories Distribution") +
  theme_void()

# Histogram of BMI values
ggplot(bmi_df, aes(x=BMI, fill=Category)) +
  geom_histogram(binwidth = 1, color="black") +
  xlab("BMI") + ylab("Number of Users") +
  ggtitle("BMI Distribution of Users") +
  theme_minimal()
