# combahton CLI
Easy access to the combahton API via a command line tool.

## Modules
* antiddos
* customer
* kvm
* login

### customer
#### invoice-all
#### invoice-unpaid
####  invoice
**Required:** invoice-id, outfile
**Usage:** cbcli customer invoice invoice-id outfile
**Example:** cbcbli customer invoice 5041234 invoice.pdf


### login
**Required:** email, apikey
**Usage:** cbcli login email apikey
**Example:** cbcli login msc@combahton.net abc1234 