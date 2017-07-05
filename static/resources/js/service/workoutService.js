'use strict';

var services = angular.module('exerciseApp');

var baseUrl = '/api/workouts/';

services.factory('WorkoutsService', function ($resource) {
    return $resource(baseUrl, {}, {
        query: {method: 'GET', isArray: true},
        create: {method: 'POST'}
    },{
        stripTrailingSlashes: false
    })
});

services.factory('WorkoutService', function ($resource) {
    return $resource(baseUrl + ':id/', {}, {
        show: {method: 'GET'},
        update: {method: 'PUT', params: {id: '@id'}},
        delete: {method: 'DELETE', params: {id: '@id'}}
    },{
        stripTrailingSlashes: false
    })
});