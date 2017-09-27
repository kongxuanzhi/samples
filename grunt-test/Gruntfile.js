module.exports = function (grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'src/<%= pkg.name %>.js',
        dest: 'build/<%= pkg.name %>.min.js'
      }
    },
    less: {
      development: {
        options: {
          paths: ['static/css']
        },
        files: {
          'dist/css/app.css': 'static/css/app.less'
        }
      }
    },
    watch: {
      scripts: {
        files: ['static/css/*.less'],
        tasks: ['less']
      }
    },
    connect: {
      server: {
        options: {
          port: 8000,
          hostname: '*',
          keepalive: true,
          base: ['./']
        }
      }
    }
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-connect');
  // Default task(s).
  grunt.registerTask('default', ['less', 'watch']);
  // grunt.registerTask('default', ['uglify']);

};
