#!/bin/bash

echo_help() {
    echo "tiktotube 0.0.1"
    echo "Usage: source tiktotube.sh [<args>]"
    echo ""
    echo "tiktok    (default) to use tiktok trending to get hashtags for outputing videos."
    echo "google    use google trends to get hashtags for outputing videos."
    echo "-h        to get this help message"
    echo ""
    echo "For full documentation see: https://github.com/AAspCodes/tiktotube#readme"
}

if [[ $# -gt 1 ]]; then
    echo "Too many arguements"
    echo_help
    return
fi

hashtag_source="tiktok"

if [[ $# == 1 ]]; then
    case $1 in

    "-h")
        echo_help
        return
        ;;

    "tiktok")
        ;;

    "google")
        hashtag_source="google"
        ;;

    *)
        echo "invalid arguement"
        echo_help
        return
        ;;
    esac
fi

# I'm not sure which is appropriate for you system.
# you can find by uncommenting the followling line
# echo $OSTYPE

# here is the link the where I found this.
## https://stackoverflow.com/questions/394230/how-to-detect-the-os-from-a-bash-script/18434831

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    pyenv activate tiktotube
    python main.py $hashtag_source
    pyenv deactivate

# elif [[ "$OSTYPE" == "linux"]]; then
    ## for Docker to be
    # do set up and run

#elif [[ $"OSTYPE" == "mysys" ]]; then
    # for Yurii
    # something like this i assume
    # virtualev activate
    # python main.py $hastag_source
    # deactivate
else
    echo "OS Type not recognized will not run"
    return
fi

echo "tiktoktube.sh is done"
