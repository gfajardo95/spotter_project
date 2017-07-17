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

        function Login(username, password, callback) {
            var jwtUrl = '/api-token-auth/';

            $http.post(jwtUrl, {username: username, password: password})
                .then(function (response) {
                    if (response.data.token) {
                        $localStorage.currentUser = {
                            username: username,
                            token: response.data.token
                        };
                        $http.defaults.headers.common.Authorization = 'Bearer ' + response.token;
                        callback(true);
                    } else {
                        callback(false);
                    }
                });
        }

        function Logout() {
            delete $localStorage.currentUser;
            $http.defaults.headers.common.Authorization = '';
        }

    });


})();