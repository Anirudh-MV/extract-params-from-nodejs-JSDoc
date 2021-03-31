# extract-params-from-nodejs-JSDoc

## To quickly document APIs written in NodeJS 

i.e. to automate extraction of all kinds of parameters from your code

Paste your code in `file.txt` and run `script.py`

The output for the dummy file.txt in the repo is 

```
The body as JSON
{
   "userid": {{userid}}
}

JSDocs format params with all 3 parameters (url param, query param and body param)
 * @param {string} userid - The userid
 * @param {string} isDisabled - The isDisabled
 * @param {string} id - The id


The query string
?isDisabled={{isDisabled}}&
```

## Known issue

This code returns all params as string in JSDoc