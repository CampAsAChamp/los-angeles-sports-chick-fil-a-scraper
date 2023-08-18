#!/bin/sh

# ------------------------------------
# Usage: source setenv.sh
# ------------------------------------
#
# Remarks:
# Use the Makefile for source'ing dotenv files - no need for a separate script.
# ------------------------------------

COLOR_ERROR=$(tput setaf 1)
COLOR_HIGHLIGHT=$(tput setaf 4)
COLOR_LOG=$(tput setaf 2)
NC=$(tput sgr0)

ENV_FILE='./env/demo.env'
if [ -f $ENV_FILE ]; then
  echo "${COLOR_LOG}Loading environment variables from${NC} ${COLOR_HIGHLIGHT}$ENV_FILE${NC} ${COLOR_LOG}(dotenv) file ...${NC}\n"

  cmd="cat $ENV_FILE | sed 's/^\(.*\)=.*/unset \1/'"

  # list the variables before doing the actual exporting:
  eval "$cmd"
  eval "eval \$($cmd)"

  echo ""
  echo "${COLOR_LOG}Done!${NC}\n"
else
  echo "${COLOR_ERROR}File not found! Unable to load dotenv file: ${COLOR_HIGHLIGHT}${ENV_FILE}${NC}"
fi
