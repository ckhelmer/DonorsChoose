
console.log("hello")
// Load plugins
// const autoprefixer = require("gulp-autoprefixer");
// const browsersync = require("browser-sync").create();
// const cleanCSS = require("gulp-clean-css");
// const del = require("del");
// const gulp = require("gulp");
// const header = require("gulp-header");
// const merge = require("merge-stream");
// const plumber = require("gulp-plumber");
// const rename = require("gulp-rename");
// const sass = require("gulp-sass");

// Load package.json for banner
//const pkg = require('./package.json');

// Set the banner content
//const banner = ['/*!\n',
//   ' * Start Bootstrap - <%= pkg.title %> v<%= pkg.version %> (<%= pkg.homepage %>)\n',
//   ' * Copyright 2013-' + (new Date()).getFullYear(), ' <%= pkg.author %>\n',
//   ' * Licensed under <%= pkg.license %> (https://github.com/BlackrockDigital/<%= pkg.name %>/blob/master/LICENSE)\n',
//   ' */\n',
//   '\n'
// ].join('');

// BrowserSync
// function browserSync(done) {
//   browsersync.init({
//     server: {
//       baseDir: "./"
//     },
//     port: 3000
//   });
//   done();
// }

// // BrowserSync reload
// function browserSyncReload(done) {
//   browsersync.reload();
//   done();
// }

// // Clean vendor
// function clean() {
//   return del(["./vendor/"]);
// }

// // Bring third party dependencies from node_modules into vendor directory
// function modules() {
//   // Bootstrap
//   var bootstrap = gulp.src('./node_modules/bootstrap/dist/**/*')
//     .pipe(gulp.dest('./vendor/bootstrap'));
//   // Font Awesome CSS
//   var fontAwesomeCSS = gulp.src('./node_modules/@fortawesome/fontawesome-free/css/**/*')
//     .pipe(gulp.dest('./vendor/fontawesome-free/css'));
//   // Font Awesome Webfonts
//   var fontAwesomeWebfonts = gulp.src('./node_modules/@fortawesome/fontawesome-free/webfonts/**/*')
//     .pipe(gulp.dest('./vendor/fontawesome-free/webfonts'));
//   // jQuery Easing
//   var jqueryEasing = gulp.src('./node_modules/jquery.easing/*.js')
//     .pipe(gulp.dest('./vendor/jquery-easing'));
//   // jQuery
//   var jquery = gulp.src([
//       './node_modules/jquery/dist/*',
//       '!./node_modules/jquery/dist/core.js'
//     ])
//     .pipe(gulp.dest('./vendor/jquery'));
//   // Simple Line Icons
//   var simpleLineIconsFonts = gulp.src('./node_modules/simple-line-icons/fonts/**')
//     .pipe(gulp.dest('./vendor/simple-line-icons/fonts'));
//   var simpleLineIconsCSS = gulp.src('./node_modules/simple-line-icons/css/**')
//     .pipe(gulp.dest('./vendor/simple-line-icons/css'));
//   return merge(bootstrap, fontAwesomeCSS, fontAwesomeWebfonts, jquery, jqueryEasing, simpleLineIconsFonts, simpleLineIconsCSS);
// }

// // CSS task
// function css() {
//   return gulp
//     .src("./scss/**/*.scss")
//     .pipe(plumber())
//     .pipe(sass({
//       outputStyle: "expanded",
//       includePaths: "./node_modules",
//     }))
//     .on("error", sass.logError)
//     .pipe(autoprefixer({
//       browsers: ['last 2 versions'],
//       cascade: false
//     }))
//     .pipe(header(banner, {
//       pkg: pkg
//     }))
//     .pipe(gulp.dest("./css"))
//     .pipe(rename({
//       suffix: ".min"
//     }))
//     .pipe(cleanCSS())
//     .pipe(gulp.dest("./css"))
//     .pipe(browsersync.stream());
// }

// // Watch files
// function watchFiles() {
//   gulp.watch("./scss/**/*", css);
//   gulp.watch("./**/*.html", browserSyncReload);
// }

// // Define complex tasks
// const vendor = gulp.series(clean, modules);
// const build = gulp.series(vendor, css);
// const watch = gulp.series(build, gulp.parallel(watchFiles, browserSync));

// // Export tasks
// exports.css = css;
// exports.clean = clean;
// exports.vendor = vendor;
// exports.build = build;
// exports.watch = watch;
// exports.default = build;

// Modal js
//$("#myModal").modal({backdrop: true})

// Essay js

// poverty level
//low
//Medium
//high
//highest

//grade level
//prek-2
//3-5
//6-8
//9-12

//total price including optional support


//students reached



// Select the submit button
var submit = d3.select("#submitbutton");
console.log("hello")
submit.on("click", function() {

 
  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node from essay
  var inputElement1 = d3.select("#povertylevel")
  
    // Get the value property of the input element
  var inputValue1 = inputElement1.property("value");
  
  var inputElement2 =d3.select("#gradelevel")
  var inputValue2 = inputElement2.property("value");

  var inputElement3 =d3.select("#totalcost")
  var inputValue3 = inputElement3.property("value");

  var inputElement4 =d3.select("#numberstudents")
  var inputValue4 = inputElement4.property("value");

  console.log(inputValue1);
  console.log(inputValue2);
  console.log(inputValue3);
  console.log(inputValue4);

  // var xhr = new XMLHttpRequest();
  // xhr.open('POST', '/get_post_json');
  // xhr.setRequestHeader('Content-Type', 'application/json');
  // xhr.onload = function() {
  //   if (xhr.status == 200) {
  //     var data = JSON.parse(xhr.responseText);
  //   }
  // };

  // xhr.send(JSON.stringify({
  //   inputValue1: 'inputValue1'
  // }))

$.ajax({
  type: 'POST',
  url: '/get_post_json',
  //contentType: "application/json",
  data: {'inputValue1' : inputValue1, 'inputValue2' : inputValue2, 'inputValue3' :inputValue3, 'inputValue4' : inputValue4},
  dataType: "json",
  success: function(response) {
    console.log(response[0]);
    if (response[0] == "0") {
      window.location.href = ("/negativeresults")
}
if (response[0] == "1") {
  window.location.href = ("/positiveresults")
}
   },
  error: function(err) {
    console.log(err)
  } 
})




});
  // Select the input element and get the raw HTML node from form
  //var inputElement1 = d3.select("#example-form-input")

