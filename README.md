# Presto Challenge
## The goal
The main challenge is to set how to handle the recoursive model relationship logic. I've decided to go for a ManyToMany recoursive field for a modifier. Prefetching humongous amount of data (each modifier can have a 10+ modifiers itself) might be an overkill and the larger the initial menu set request - the larger the processing and response time will be. Especially considering we cannot possibly show 100+ options on a single screen on a frontend. I would rather make an addional request to fetch the modifiers of a chosen menu item modifier if the end user ever choses that option.

## Trade-offs
* I would add an authorization and limit the menu items per restaurant customer
* User roles. Customers should not be creating or changing menu items using the api
* Right now the proper save and update calls for entities relations over the api does not work
* Environment support. dotenv python package provides an easy environment management
* Test. There is not much logic, but api request call test operating over the fixtures would certanly be a plus
* Impovement over docker-compose file and linking it up with the environment settings
* API versioning is something that needs to be considered from the beginning
