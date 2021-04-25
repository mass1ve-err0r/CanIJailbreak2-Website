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

All the Jailbreaks are listed inside the `jailbreaks.py` file under the JailbreakMap as dictionary.

Here's an example with the checkra1n utility:
```
{
	"name": "checkra1n",              <- Jailbreak Name
	"current_version": "0.12.2",      <- Current Version
	"url": "https://checkra.in",      <- Website or theiphonewiki link
	"minimum_ios": "12.0",            <- Minimum required iOS
	"maximum_ios": "14.4.2",          <- Maximum supported iOS
	"minimum_pg": "5S",               <- Oldest supported device
	"maximum_pg": "X",               <- Latest supported device
	"type": "Semi-Tethered",          <- Jailbreak Type
	"platforms": ['apple', 'linux'],  <- List of supported platforms
	"notes": ["..."]                  <- Additional notes (f.e. version exclusions)
}
```
The fields `minimum_pg` and `maximum_pg` are essentially the processors but I opted to keep the device name and classify similar devices to the same name. It seems confusing at first but peeking at the `DeviceMapPG` in `device_helper.py` might make that more clear.

_(This is subject to rewrite and any contribution is welcome in terms of design!)_

If a new Jailbreak appears, just create a dictionary object as above (without the annotations) and PR it. Currently some legacy Jailbreaks below iOS 6 are _not_ listed but welcome as PR.


**The only rule I have is to exclude unstable or experimental Jailbreaks. Any fraudulent / copycat Jailbreaks such as Th0r are strictly prohibited and these PRs will be rejected.**

## API Docs
#### **THIS ENDPOINT REQUIRES AUTHENTICATION.**

I tried to keep the API access pretty easy and self-explanatory so it works without any wild parsing.

Here's the potential return codes which get returned as json in the field `status`:
- -1: Failure. No further data
- 1: Query Successfully accepted **BUT** device _not_ found. No further data
- 2: Query Successfully accepted **BUT** given iOS version was out-of-bounds. You will receive the following data (json):
	- <details>
		<summary> show exemplary return iPhone 5S & 13.0 </summary>

		```
		{
			"status": 2,
			"minimum_ios": "7.0",
			"maximum_ios": "12.5.1"
		}
		```
	</details>
- 0: Query Successfully accepted. You will have a field called `jelbreks` which is a list of objects formatted as shown in the _Contributing_ section.

Example:
Query: `https://canijailbreak2.com/v1/pls/iPhone 12 Pro Max/14.3`

<details>
	<summary>Show Result</summary>

```
{
	"status": 0,
	"jelbreks": [
		{
			"name": "Taurine",
			"url": "https://taurine.app",
			"current_version": "1.0.4",
			"minimum_ios": "14.0",
			"maximum_ios": "14.3",
			"minimum_pg": "6S",
			"maximum_pg": "12",
			"type": "Semi-Untethered",
			"platforms": ["apple"]
		},
		{
			"name": "unc0ver",
			"url": "https://unc0ver.dev",
			"current_version": "6.1.2",
			"minimum_ios": "11.0",
			"maximum_ios": "14.3",
			"minimum_pg": "6S",
			"maximum_pg": "12",
			"type": "Semi-Untethered",
			"platforms": ["apple"],
			"notes": ["iOS12 A12 is between 12.0 - 12.3 and 12.4 - 12.4.1"]
		}
	]
}
```
</details>

## Installation + Setup
You wish to run your own instance? No problemo.

Make sure you got a Linux VPS with python3 (3.6+) installed. Create a virtal environment and install the deps from `req.txt` and you're ready to go!

If you'd like to provide API access, make sure you have a `.env` with tokens. See `api.py` for further details on that.

_(Recommended)_ run it with PM2 for easier management!


## Credits
- chpwn for the original idea
- [Callum Jones](https://github.com/cj123) for the first implementation and keeping it OSS
- TheMasterOfMike, hopolapopola, aaronp613, Cameren and Jessie O. for constantly watching over the correctness of information
- Local Pigeons for the good support and being fluffy companions

## License
This project is licensed under **MIT**. Have fun!
