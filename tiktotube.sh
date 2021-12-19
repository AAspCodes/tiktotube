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

pyenv activate tiktotube
python main.py $1
pyenv deactivate
echo $hashtag_source
echo "done"
