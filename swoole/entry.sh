#!/bin/ash
APP_PATH="/source"
APP_BASH_ENTRY=$APP_PATH"/app.sh"
if [ -e $APP_BASH_ENTRY ]; then
    /bin/ash $APP_BASH_ENTRY
else
    echo "No App Entry"
fi
