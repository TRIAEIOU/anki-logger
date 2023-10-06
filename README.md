# Anki logger

Simple [Anki](https://apps.ankiweb.net) [addon]() ([source](https://github.com/TRIAEIOU/anki-logger)) that writes Anki stdout and stderr to a timestamped log file in `<addon directory>/user_files`.

## Use case

Find hard to trigger bugs during addon testing in production environment (i.e. you've made an addon that you are using in your normal Anki activities and it sometimes crashes but you are unsure why).