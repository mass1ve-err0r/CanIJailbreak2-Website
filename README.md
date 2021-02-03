# Can I Jailbreak 2
> Python 3.7+ | Fast | Powered by you

## Prelude
[Callum Jones](https://github.com/cj123) has provided us  over the years with canijailbreak.com, a source to find out whether you can jailbreak your iDevice or not.

In recent times I found that it wasn't updated and thus I just wanted to create an alternative to it.

This is just that: An entire rewrite, run by sanic and powered by your contributions to keep it up to date!

## Features
- Entire rewrite with a _(subjectively)_ nice new look
- API for easy access with f.e. (discord) bots
	- You can request access to the API by just sending me a DM on twitter @saadat603
- Easily expandable

## Contributing
A new jailbreak arrived and it's not on the site? Missing a legacy Jailbreak? -- No problem!

All the Jailbreaks are listed inside the `SiteHelper.py` file under the JailbreakMap as dictionary.

Here's an example with the checkra1n utility:
```
{
	"name": "checkra1n",              <- Jailbreak Name
	"url": "https://checkra.in",      <- Website or theiphonewiki link
	"minIOS": "12.0",                 <- Minimum required iOS
	"maxIOS": "14.3",                 <- Maximum supported iOS
	"minProc": "5S",                  <- Oldest supported device
	"maxProc": "X",                   <- Latest supported device
	"type": "Semi-Tethered",          <- Jailbreak Type
	"platforms": ['apple', 'linux']   <- List of supported platforms
}
```
The fields `minProc` and `maxProc` are essentially the processors but I opted to keep the device name and classify similar devices to the same name. It seems confusing at first but peeking at the `APIMap` in `SiteHelper.py` might make that more clear.

_(This is subject to rewrite and any contribution is welcome in terms of design!)_

If a new Jailbreak appears, just create a dictionary object as above (without the annotations) and PR it. Currently some legacy Jailbreaks below iOS 6 are _not_ listed but welcome as PR.


**The only rule I have is to exclude unstable or experimental Jailbreaks. Any fraudulent / copycat Jailbreaks such as Th0r are strictly prohibited and these PRs will be rejected.**

## API Docs
#### **THIS ENDPOINT REQUIRES AUTHENTICATION.**

I tried to keep the API access pretty easy and self-explanatory so it works without any wild parsing.

Here's the potential return codes which get returned as json in the field `status`:
- -1: Failure. No further data
- 1: Query Successfully accepted **BUT** device _not_ found. No further data
- 0: Query Successfully accepted. You will have a field called `jelbreks` which is a list of objects formatted as shown in the _Contributing_ section.

Example:
Query: `https://canijailbreak2.com/v1/pls/iPhone SE 1/13.4`

<details>
	<summary>Show Result</summary>

```
{
	"status": 0,
	"jelbreks": [
		{
			"name": "checkra1n",
			"url": "https://checkra.in",
			"minIOS": "12.0",
			"maxIOS": "14.3",
			"minProc": "5S",
			"maxProc": "X",
			"type": "Semi-Tethered",
			"platforms": ["apple","linux"]
		},
		{
			"name": "Odyssey",
			"url": "https://theodyssey.dev",
			"minIOS": "13.0",
			"maxIOS": "13.7",
			"minProc": "6S",
			"maxProc": "11",
			"type": "Semi-Untethered",
			"platforms": ["apple"]
		},
		{
			"name": "unc0ver",
			"url": "https://unc0ver.dev",
			"minIOS": "11.0",
			"maxIOS": "13.5",
			"minProc": "5S",
			"maxProc": "11",
			"type": "Semi-Untethered",
			"platforms": ["apple"]
		}
	]
}
```
</details>

## Installation + Setup
You wish to run your own instance? No problemo.

Make sure you got a Linux VPS with python3 (3.6+) installed. Create a virtal environment and install the deps from `req.txt` and you're ready to go!

If you'd like to provide API access, make sure you have a `.env` with tokens. See `API.py` for further details on that.

_(Recommended)_ run it with PM2 for easier management!


## Credits
- chpwn for the original idea
- [Callum Jones](https://github.com/cj123) for the first implementation and keeping it OSS
- Local Pigeons for the good support and being fluffy companions

## License
This project is licensed under **MIT**. Have fun!
