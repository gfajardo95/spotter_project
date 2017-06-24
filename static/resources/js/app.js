/**
 * Created by gfaja on 5/16/2017.
 */

(function () {
    'use strict';

    var app = angular.module('exerciseApp', ['ngRoute', 'ngResource']);

    app.config(function ($routeProvider) {

        $routeProvider
            .when("/", {
                templateUrl: "static/resources/html/home.html",
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
})();