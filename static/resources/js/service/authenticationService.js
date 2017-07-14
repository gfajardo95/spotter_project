/**
 * Created by gfaja on 7/14/2017.
 */

(function () {
    'use strict';

    var services = angular.module('exerciseApp');

    services.factory('AuthenticationService', function ($http, $localStorage) {
        var service = {};

        service.Login = Login;
        service.Logout = Logout;

        return service;

        function Login(){
            var jwtUrl = 'api/api-token-auth'
        }

        function Logout(){

        }

    });


})();