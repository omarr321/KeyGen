# Key Generator
This is a basic key generator that allows you to create, save, and check valid keys
## Key Creation
The Key Creation is simple. It will generate a new 17-digit key that was never used before
## Key Saving
The Key Saving allows you to save keys to a file
## Checking Vaild Keys
If you put in a 17-digit key, it will check to see if it is a valid key by seeing if it has been generated before and passing the Key validation
## Key Vailding
You do not need to worry about key validation because it is done automatically. The key validation is based on 8 criteria that the key must meet:
1. No digit can be zero
1. The first digit is the sum of all other digit. Then the sub of that numbers didgit is taken again. This continues until it is a single digit long
1. The digits 2-5 when summed up must be an even number
1. The digits 2-5 when mutipled together must be a mutiple of 5
1. The digits 6-11 when summed up must be an odd number
1. The digits 6-11 when mutipled together must be a mutiple of 7
1. The digits 12-17 when summed up must be an odd number
1. The digits 12-17 when mutipled together mush be a mutiple of 12