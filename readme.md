[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11421186&assignment_repo_type=AssignmentRepo)
# HW. 1 Currency Conversion

You are working as a software developer at a currency exchange company call AUPP Currency EX.
Your manager assigned you to create an application that can handle transactions below:

- Exchange from USD to RIEL, USD rate=4000៛.
- Exchange from YUAN to RIEL, YUAN rate=643៛.
- Exchange from BATH to RIEL, BATH rate=123៛.

<br>

## Technical requirement (condition):

The application development team required you to create a function call currency_conversion that take 2 parameters, **(Currency and Amount)**.

Make sure that currency_conversion function return the following value in different situation:

1. When invalid currency provided, make sure the function return **‘Not Found’**
2. If the amount is not number type, make sure the function return **‘Invalid Amount’**
3. If both parameters are correct, return convert value from the function example:
   > - currency_conversion('USD', 2) # function should return 8000

<br>

### Task: Your task is to create an application that help user to currency of their choice to Reil.

<br>

### Instruction:

> - In the main file ask for user inputs
>   > Input:
>   >
>   > - Ask user to pick the desire currency (with option display)
>   > - Ask user to pick the desire amount to convert
> - Do a calculation according to user input by multiplying the input with the desire currency (ex: currency \* amount)
> - Then display result in a creative way.

### Expected Output:

![HW_1_Currency](HW_1_Currency.png)

### HINT:

> - Create 2 files:
>   1. One that contain function for currency [backend]
>   2. The other to ask for user input and calling back function for calculation [frontend]
> - Call the function to the main file.

<br><br>

<h1 style="text-align: center;">*** Be Creative ***</h1>
