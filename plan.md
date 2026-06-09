on start

generate dots (distributed evenly across scene) -- done

on wave release

r add force to impact dot
r remove force from impact dot = to # of connections * reducer ratio
r add force = to reducer ratio of impact to each connected dot
r propagate

c turn overloaded dots red
c remove overloaded dots

ui

c wave strength slider
r release wave button
r reset button

r clicking two dots creates a link between them
r middle click gives info on dot clicked

c right click to place wave epicenter
