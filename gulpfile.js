// 引用gulp包
var gulp    = require('gulp');
// var concat  = require('gulp-concat');
// var haml    = require('gulp-haml');
// var babel   = require('gulp-babel');
// var sass    = require('gulp-sass');
// var reload  = require('gulp-livereload');
// var rename  = require('gulp-rename');
// var zipjs   = require('gulp-uglify');
// var zipcss  = require('gulp-minify-css');

gulp.task('build-libcss', ['build-source'], function() {
  var libCssList = [
    'data_static/components/bootstrap/dist/css/bootstrap.css',
    'data_static/components/bootstrap/dist/css/bootstrap-theme.css',
  ];
  gulp.src(libCssList)
    .pipe(concat('lib.css'))
    .pipe(gulp.dest('data_static/build'))
    .pipe(zipcss())
    .pipe(rename({ suffix: '.min'}))
    .pipe(gulp.dest('data_static/build'));
});

gulp.task('build-libjs', ['build-source'], function() {
  var libJsList = [
    'data_static/components/angular/angular.js',
    'data_static/components/jquery/dist/jquery.js',
    'data_static/components/lodash/lodash.js',
    'data_static/components/bootstrap/dist/js/bootstrap.js',
  ];
  gulp.src(libJsList)
    .pipe(concat('lib.js'))
    .pipe(gulp.dest('data_static/build'))
    .pipe(zipjs())
    .pipe(rename({ suffix: '.min'}))
    .pipe(gulp.dest('data_static/build'));
});

gulp.task('build-libfont', function() {
  gulp.src(['data_static/components/bootstrap/fonts/*'])
    .pipe(gulp.dest('data_static/fonts'));
});

gulp.task('build-lib', ['build-libcss', 'build-libjs', 'build-libfont'], function() {

});

gulp.task('build-haml', function() {
  gulp.src('./data_static/source/**/*.haml')
    .pipe(haml({compiler: 'visionmedia'}))
    .pipe(haml())
    .pipe(gulp.dest('./data_static/build'))
    .pipe(reload());
});

gulp.task('build-es6', function() {
  gulp.src('./data_static/source/**/*.es6')
    .pipe(babel())
    .pipe(gulp.dest('./data_static/build'))
    .pipe(reload());
});

gulp.task('build-sass', function() {
  gulp.src('./data_static/source/**/*.sass')
    .pipe(sass())
    .pipe(gulp.dest('./data_static/build'))
    .pipe(reload());
});

gulp.task('build-source', ['build-haml', 'build-es6', 'build-sass'], function() {
});

gulp.task('build-app', function() {
  gulp.src('./data_static/source/app/*.es6')
    .pipe(babel())
    .pipe(concat('app.js'))
    .pipe(gulp.dest('data_static/build'))
    .pipe(zipjs())
    .pipe(rename({ suffix: '.min'}))
    .pipe(gulp.dest('data_static/build'));
  gulp.src('./data_static/source/app/*.sass')
    .pipe(sass())
    .pipe(concat('app.css'))
    .pipe(gulp.dest('data_static/build'))
    .pipe(zipcss())
    .pipe(rename({ suffix: '.min'}))
    .pipe(gulp.dest('data_static/build'));
});

gulp.task('build-all', ['build-lib', 'build-source', 'build-app']);

gulp.task('dev', ['build-all'], function() {
  reload.listen();
  gulp.watch(['./data_static/source/**/*.haml'], ['build-haml']);
  gulp.watch(['./data_static/source/**/*.es6'], ['build-es6']);
  gulp.watch(['./data_static/source/**/*.sass'], ['build-sass']);
  gulp.watch(['./data_static/source/app/**/*.es6'], ['build-app']);
  gulp.watch(['./data_static/source/app/**/*.sass'], ['build-app']);
});

gulp.task('deploy', function() {

});
