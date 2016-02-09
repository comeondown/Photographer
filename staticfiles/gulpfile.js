var gulp = require('gulp');
var less = require('gulp-less');
var path = require('path');

gulp.task('default', function(){
	gulp.watch('less/**', function(event){
		gulp.run('styles');
	});

});

gulp.task('styles', function(){
	return gulp.src('./less/styles.less')
		.pipe(less({
			paths: [path.join(__dirname, 'less', 'includes') ]
		}))
		.pipe(gulp.dest('./css'))
});
