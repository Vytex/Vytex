from flask import Flask, render_template, request

app = Flask(__name__)

# root to index
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lineList')
def lineList():
    results = [
        ["Test Venue", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"], "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae nisi vel odio aliquet placerat viverra ac sem. Curabitur sodales justo id elit eleifend tristique. Aenean lacinia massa at neque gravida vehicula. Vestibulum ultricies, elit consectetur fringilla egestas, quam ante aliquam sem, vel pellentesque lacus tellus a metus. Praesent vel augue metus. Vivamus ac dapibus massa. Curabitur semper scelerisque purus. Curabitur iaculis venenatis massa, sit amet fermentum leo consectetur sed. Pellentesque convallis justo pellentesque, laoreet odio posuere, auctor leo. Sed non consequat ante. Donec tristique, est in vulputate gravida, tortor mi blandit ante, nec molestie est mi in libero. Suspendisse at nisl a leo laoreet ultrices. Suspendisse eget diam id risus hendrerit imperdiet.\
                                                                                                \
                                                                                                Donec eleifend velit vel orci accumsan, vel bibendum justo tincidunt. Cras tempor eleifend orci sit amet convallis. Praesent nisi mauris, posuere vitae lorem at, vestibulum varius eros. Nulla facilisi. Mauris fringilla nec tellus ut suscipit. Aenean turpis leo, tristique et vehicula in, venenatis at tortor. Nulla quam nulla, aliquet vel euismod eget, auctor quis augue. Donec sit amet gravida mi, vitae ullamcorper velit. Ut sed sollicitudin mauris. Sed eu justo vitae leo scelerisque pharetra. Nulla non purus vulputate, accumsan mi ac, bibendum neque. Phasellus sed dui molestie, laoreet mi ut, molestie quam.\
                                                                                                \
                                                                                                Aliquam sit amet massa erat. Nam consequat ornare ante eu luctus. Phasellus eu venenatis orci. Phasellus efficitur, arcu sed rhoncus aliquam, turpis sem facilisis quam, id pharetra purus neque non magna. Maecenas quis pulvinar mi. Pellentesque sed neque leo. Nullam pharetra ex libero, ut egestas risus gravida eu. Aliquam erat volutpat.\
                                                                                                \
                                                                                                Vestibulum varius leo mi, sed accumsan sem tristique id. Vivamus ornare blandit magna, et mattis ex varius at. Nam at ullamcorper orci, at pharetra justo. Cras nec iaculis elit, vel congue tortor. Pellentesque est quam, viverra a justo nec, sodales pharetra lorem. Nunc eget arcu id leo bibendum convallis. Vestibulum felis nunc, pharetra sit amet mollis ut, mattis non ipsum. Nulla blandit dictum elit, in suscipit dolor rhoncus sed. Fusce nulla nisl, sollicitudin varius efficitur laoreet, maximus id lacus. Proin lacinia malesuada nisl a viverra. Curabitur hendrerit, arcu et blandit sagittis, elit arcu congue tellus, pharetra vulputate risus nunc et ipsum. Maecenas tempus orci in ex hendrerit, id aliquet lectus luctus. Praesent placerat eros non rutrum placerat. Ut vel rhoncus mi.\
                                                                                                \
                                                                                                In finibus ultricies imperdiet. Duis auctor quam a urna laoreet consequat. Suspendisse ut lacus a lorem luctus fringilla et id magna. Proin eleifend nulla non sapien imperdiet faucibus. Proin elementum sodales urna, ac faucibus magna laoreet scelerisque. Aliquam nisl nibh, feugiat ac imperdiet ac, facilisis sit amet nisi. Nullam pharetra sit amet mauris in suscipit. Aliquam orci lorem, dapibus quis cursus sed, rutrum eu sapien. Donec porttitor ipsum tortor, quis fermentum lacus lobortis vel. Suspendisse euismod pretium orci, vitae scelerisque neque. Suspendisse vel nisi ut libero lacinia eleifend. Fusce iaculis volutpat leo vel cursus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras id pharetra ligula. Donec lacinia rhoncus malesuada. Vivamus accumsan sed quam quis consequat. Donec sit."],
        ["Test Venue2", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue3", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue2", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue2", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue2", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue2", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue2", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue2", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue2", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue2", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue2", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]],
        ["Test Venue last", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]]

    ]
    
    return render_template("lineList.html", results=results)

if  __name__ == "__main__":
    app.run(debug=True)