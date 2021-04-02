from terrasnek.api import TFC
import os

###
# Documentation of the Py client libry
# https://terrasnek.readthedocs.io/en/latest/
###

TFC_TOKEN = os.getenv("TFC_TOKEN", None) 
TFC_URL = os.getenv("TFC_URL", None)  #  https://app.terraform.io
TFC_ORG = os.getenv("TFC_ORG") # org: paulm

if __name__ == "__main__":
    api = TFC(TFC_TOKEN, url=TFC_URL)
    api.set_org("TFC_ORG")
    ws = api.workspaces.list
    ## Get the WS ID / Help here to get the id
    ws_id = api.workspaces(workspace_name="terraform-paulm-org") #.id
    ## Get the Run ID 
    run_show_list= api.runs.show(ws_id)
    ## Filter the last run
    run_id = api.runs.list_all(ws_id)[0]
    ## Apply the plan 
    applied_run = api.runs.apply(run_id)