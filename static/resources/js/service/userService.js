/**
 * Created by gfaja on 7/22/2017.
 */

(function(){
'use strict';

var services = angular.module('exerciseApp');
var userUrl = '/api/users/';

services.factory('UserService', function ($resource) {
    return $resource(userUrl, {}, {
        query: {method: 'GET', isArray: true}
    })
});

}());