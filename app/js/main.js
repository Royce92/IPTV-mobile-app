/* model */
var m3u8model = Backbone.Model.extend({
    defaults: function(){
        return {
            channel: "",
            url: ""
        }
    }

    });
/* Collection */


var m3u8collection = Backbone.Collection.extend({

    model: m3u8model, /* binding the model to the collection */
    url: "m3u8.json", /* path to Json File */

    parse: function(response){
    return response.channels;
    }
        });

var moviesViews = Backbone.View.extend({
    el: "movies"
    
    });



var tvViews = Backbone.View.extend({
  el: "#tv",

    collection: new m3u8collection(), /* bind Collection into the view*/

/* Benging fetching collection uppon the view initiation */

    initialize: function(){
                
    var self = this;
   this.collection.fetch({ /*underscore fetch method, to fetch the json objects from the collection*/
      success: function() { /* if fetch success continue */
        self.render();
      }
    });        
    },
  
  /* Events */

    events:{
        "click": "onClick"
        
    },

    onClick: function(e) {
        var link = ($(e.target).attr('href'));
        e.preventDefault();
        var vid = new VideoView({pos: link, el: "#video1"});
        vid.render();
        $("#video1").load();
        this.$el.append(myVideo.play());
    },
    
    
/* End of Events */
   
   /* End View initiation, and fetch pass the values to the render method. */
   
     render: function() {
    var scope = this;
    this.collection.forEach(function(model) {
      scope.output(model);
    });
    return this; 
  },

  output: function(model) {
    var row = document.createElement("li");
    row.innerHTML =  " <a href="+ model.get("url")+">"+ model.get("channel")+"</a>";    
    this.el.appendChild(row);

  }
});

var VideoView = Backbone.View.extend({
    initialize: function (attrs) {
    this.options = attrs;
}, 
    render: function(){
         this.$el.html(" <source src="+this.options.pos+">"+"type="+"application/x-mpegURL>");    
       return this;            
    }
        
    });
$(document).ready(function () {

    
var app = new tvViews();

});

