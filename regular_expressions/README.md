# Regular Expressions (Ruby)

Ruby scripts that each take one command-line argument and print the parts of it that match a regular expression, using `String#scan`.

## Usage

```
./0-simply_match_school.rb "Best School" | cat -e
School$
```

Make the scripts executable first: `chmod +x *.rb`

## Files

| File | Regex | Matches |
|---|---|---|
| `0-simply_match_school.rb` | `/School/` | the word `School` |
| `1-repetition_token_0.rb` | `/hbt{2,5}n/` | `hb`, then 2 to 5 `t`, then `n` |
| `2-repetition_token_1.rb` | `/hb?tn/` | `htn` and `hbtn` |
| `3-repetition_token_2.rb` | `/hbt+n/` | `hb`, then 1 or more `t`, then `n` |
| `4-repetition_token_3.rb` | `/hbt*n/` | `hb`, then 0 or more `t`, then `n` (no square brackets) |
| `5-beginning_and_end.rb` | `/^h.n$/` | `h`, any single character, `n` |
| `6-phone_number.rb` | `/^\d{10}$/` | a 10-digit phone number |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | `/[A-Z]/` | capital letters only |
| `8-textme.rb` | `/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/` | prints `[SENDER],[RECEIVER],[FLAGS]` from a TextMe log line |
| `9-passed_linkedin_regex_challenge.jpg` | | screenshot of the completed LinkedIn regex puzzle |

## Author

sanol-1
