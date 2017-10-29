/**
 * Created by gfaja on 5/16/2017.
 */

(function () {
    'use strict';

    var app = angular.module('exerciseApp', ['ngRoute', 'ngResource', 'ngStorage']);

    app.config(function ($routeProvider, $resourceProvider, $httpProvider) {

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $resourceProvider.defaults.stripTrailingSlashes = false;

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
            .when("/login", {
                templateUrl: "static/resources/html/login.html",
                controller: "LoginCtrl"
            })
            .otherwise({
                redirectTo: "/"
            });
    });

    app.run(function($location, $localStorage, $http, $rootScope, AuthenticationService){
        if ($localStorage.currentUser){
            $http.defaults.headers.common['Authorization'] = 'JWT ' + $localStorage.currentUser.token;
            $rootScope.isSignedIn = true;
        }else{
            $rootScope.isSignedIn = false;
        }

        $rootScope.signOut = function (){
            AuthenticationService.Logout();
            $rootScope.isSignedIn = false;
            $location.path('/');
        }
    });

})();