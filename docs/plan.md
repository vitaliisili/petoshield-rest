## Tables
users
pets
policies (sold/paid)
insurance payments (income)
policies (offers)
insurance rates
insured cases
medical (non-medical) services provided
medical (non-medical) invoices
medical payments (outcome)
medical facilities (services providers)
services proposed
additional table- blog
articles
## Interfaces
**user** (two interfaces - public and private)
- crud profile
- crud pet
- choose policy from offers
- pay insurance company's invoices
- see invoices (paid/unpaid)
- see financial stats
**service provider**
- check policy's validity
- register case
- service client
- issue invoice acording to services provided
**insurance manager**
- issue offers (draft policies)
- change algorithm of insurance rate calculation
- see service providers invoices
- review insurance cases
- control billing system
**billing system** (robot)
- controll insurance payments
- issue invoices
- send reminders to policyholders (clients)
- pay service invoices
## Pages
### Most Important
Main
User profile (public / private)
Policy offers
Get rate
### Optional
Service providers (list, profile)
Blog (list, post)
About insurance company (?)
Contacts
### Very Optional
Service provider admin page - can be provided by `admin.site`
Insurance manager admin page - can be provided by `admin.site`
Content provider admin page (?) - brands who want to place their articles in our blog
PS: