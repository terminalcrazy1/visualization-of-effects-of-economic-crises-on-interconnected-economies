on start

generate dots (distributed evenly across scene) -- done

on wave release

add force to impact dot
remove force from impact dot = to # of connections * reducer ratio
add force = to reducer ratio of impact to each connected dot
propagate
turn overloaded dots red
remove overloaded dots

ui

wave strength slider
release wave button (right click to place epicenter?)
reset button