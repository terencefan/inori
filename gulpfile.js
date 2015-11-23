// 引用gulp包
var gulp    = require('gulp');
var concat  = require('gulp-concat');
var jade = require('gulp-jade');
var babel   = require('gulp-babel');
var sass    = require('gulp-sass');
var reload  = require('gulp-livereload');
var rename  = require('gulp-rename');
var zipjs   = require('gulp-uglify');
var zipcss  = require('gulp-minify-css');

gulp.task('build-libcss', ['build-source'], function() {
  var libCssList = [
  ];
  gulp.src(libCssList)
    .pipe(concat('lib.css'))
    .pipe(gulp.dest('static/build'))
    .pipe(zipcss())
    .pipe(rename({ suffix: '.min'}))
    .pipe(gulp.dest('static/build'));
});

gulp.task('build-libjs', ['build-source'], function() {
  var libJsList = [
    'node_modules/angular/angular.js',
  ];
  gulp.src(libJsList)
    .pipe(concat('lib.js'))
    .pipe(gulp.dest('static/build'))
    .pipe(zipjs())
    .pipe(rename({ suffix: '.min'}))
    .pipe(gulp.dest('static/build'));
});

gulp.task('build-libreq', function() {
});

gulp.task('build-lib', ['build-libcss', 'build-libjs', 'build-libreq'], function() {

});

gulp.task('build-html', function() {
  gulp.src('static/source/**/*.jade')
    .pipe(jade())
    .pipe(gulp.dest('static/build'))
    .pipe(reload());
});

gulp.task('build-js', function() {
  gulp.src('static/source/**/*.es6')
    .pipe(babel())
    .pipe(gulp.dest('static/build'))
    .pipe(reload());
});

gulp.task('build-css', function() {
  gulp.src('static/source/**/*.sass')
    .pipe(sass())
    .pipe(gulp.dest('static/build'))
    .pipe(reload());
});

gulp.task('build-source', ['build-html', 'build-js', 'build-css'], function() {
});

gulp.task('build-app', function() {
  gulp.src('static/source/app/*.es6')
    .pipe(babel())
    .pipe(concat('app.js'))
    .pipe(gulp.dest('static/build'))
    .pipe(zipjs())
    .pipe(rename({ suffix: '.min'}))
    .pipe(gulp.dest('static/build'));
  gulp.src('static/source/app/*.sass')
    .pipe(sass())
    .pipe(concat('app.css'))
    .pipe(gulp.dest('static/build'))
    .pipe(zipcss())
    .pipe(rename({ suffix: '.min'}))
    .pipe(gulp.dest('static/build'));
});

gulp.task('develop', ['build-lib', 'build-source', 'build-app']);

gulp.task('deploy', ['build-lib', 'build-source', 'build-app']);

gulp.task('dev', ['develop'], function() {
  reload.listen();
  gulp.watch(['static/source/**/*.jade'], ['build-html']);
  gulp.watch(['static/source/**/*.es6'], ['build-js']);
  gulp.watch(['static/source/**/*.sass'], ['build-css']);
  gulp.watch(['static/source/app/**/*.es6'], ['build-app']);
  gulp.watch(['static/source/app/**/*.sass'], ['build-app']);
});
