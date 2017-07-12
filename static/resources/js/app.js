/**
 * Created by gfaja on 5/16/2017.
 */

(function () {
    'use strict';

    var app = angular.module('exerciseApp', ['ngRoute', 'ngResource']);

    app.config(function ($httpProvider, $routeProvider) {

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $routeProvider
            .when("/", {
                templateUrl: "static/resources/html/home.html",
                controller: "WorkoutListCtrl"
            })
            .when("/dashboard", {
                templateUrl: "static/resources/html/dashboard.html",
                controller: "WorkoutListCtrl"
            })
            .when("/createWorkout", {
                templateUrl: "static/resources/html/createWorkout.html",
                controller: "WorkoutCreationCtrl"
            })
            .otherwise({
                redirectTo: "/"
            });
    });

    /*app.run(function ($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    });*/

})();