# Step 1–3: Assign using "=" and print
var1 = "hello"
print(var1)        # Output: "hello"

# Step 4–5: Assign using "<-" and print
var2 <- "hello"
print(var2)        # Output: "hello"

# Step 6–7: Assign using "->" and print
"hello" -> var3
print(var3)        # Output: "hello"

# Step 8: Class of var1
print(class(var1)) # Output: "character"

# Step 9: List all variables
print(ls())

# Step 10: Remove var3
rm(var3)

# Step 11: Try printing var3 (should give error)
try(print(var3))   # Output: Error in print(var3): object 'var3' not found

# Step 12–13: Boolean TRUE
bool1 <- TRUE
print(bool1)             # Output: TRUE
print(class(bool1))      # Output: "logical"

# Step 14–15: Boolean FALSE
bool2 <- FALSE
print(bool2)             # Output: FALSE
print(class(bool2))      # Output: "logical"

# Step 16–17: Numeric
weight <- 63.5
print(weight)            # Output: 63.5
print(class(weight))     # Output: "numeric"

# Step 18–19: Another numeric
height <- 182
print(height)            # Output: 182
print(class(height))     # Output: "numeric"

# Step 20–21: Integer type with L suffix
integer_variable <- 186L
print(class(integer_variable))  # Output: "integer"

# Step 22–23: Complex number
complex_value <- 3 + 21i
print(class(complex_value))     # Output: "complex"

# Step 24–25: Character string
fruit <- "Apple"
print(class(fruit))             # Output: "character"

# Step 26–27: Single character
my_char <- 'A'
print(class(my_char))           # Output: "character"

# Step 28: Convert to raw
raw_variable <- charToRaw("Welcome to Programiz")

# Step 29: Print raw variable and class
print(raw_variable)             # Output: 57 65 6c 63 6f 6d ...
print(class(raw_variable))      # Output: "raw"

# Step 30: Convert back to character
char_variable <- rawToChar(raw_variable)

# Step 31: Print character variable and class
print(char_variable)            # Output: "Welcome to Programiz"
print(class(char_variable))     # Output: "character"

# Step 32: End of program
cat("✅ Program executed successfully.\n")

# Sample data frame
df <- data.frame(
  Name = c("Asha", "Balu", "Cyril", "Deepa"),
  Age = c(25, 19, 32, NA),
  Gender = c("Female", "Male", "Male", "Female")
)

# Show all data
print("Original Data:")
print(df)

# Filter: Age > 20
print("Age > 20:")
print(df[df$Age > 20, ])

# Filter: Gender is Female
print("Only Females:")
print(df[df$Gender == "Female", ])

# Filter: Non-missing Age
print("Rows with valid Age:")
print(df[!is.na(df$Age), ])

