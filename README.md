# microsoft-rewards-checker

A tool to send emails alerting if Microsoft Rewards aren't completed.

## Installation

Install the requirements.

```shell
pip install -r requirements.txt
```

1. Create an `.env` file by copying [.template.env](.template.env) to a new file named `.env` and fill out with your
   information.
   Gmail is the only tested SMTP currently, see [this](https://www.gmass.co/blog/gmail-smtp/) for how to set up.
2. You'll need a Chrome profile with your Bing account logged-in.
   It may be useful to create a new one.

## Usage

```shell
pytest test_verifyallsearchesdone.py
```

If all searches are complete, you won't get an email. If all searches aren't complete, you will get an email.

[Schedule this job](https://stackoverflow.com/q/30835547/4164390), whether via a cron, Windows Task Scheduler, etc.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Roadmap

1. Share Windows Task Scheduler config