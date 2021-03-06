/**
 * Created by gfaja on 5/16/2017.
 */

(function () {
    'use strict';

    var app = angular.module('exerciseApp');

    app.controller('WorkoutListCtrl', ['$scope', 'WorkoutService', 'WorkoutsService', function ($scope, WorkoutService, WorkoutsService) {
        $scope.isBusy = false;
        $scope.successMessage = "";
        $scope.errorMessage = "";

        var crudInit = function () {
            $scope.isBusy = true;
            $scope.successMessage = "";
            $scope.errorMessage = "";
        };

        $scope.cancel = function () {
            $scope.isBusy = false;
            $scope.editing = false;
        };

        //READ
        var onReadWorkoutComplete = function (data) {
            $scope.workouts = data;
            if ($scope.workouts.length === 0) {
                $scope.successMessage = "There are no workouts to display."
            }
        };

        var onReadError = function () {
            $scope.errorMessage = "Error getting the workouts."
        };

        var onReadFinally = function () {
            $scope.isBusy = false;
        };

        /*callback for ng-click 'getAllWorkouts': */
        $scope.getAllWorkouts = function () {
            crudInit();

            $scope.workouts = WorkoutsService.query()
                .$promise
                .then(onReadWorkoutComplete, onReadError)
                .finally(onReadFinally);
        };

        //UPDATE
        var onUpdateWorkoutComplete = function () {
            $scope.successMessage = "Workout updated succesfully!"
        };

        var onUpdateError = function () {
            $scope.errorMessage = "Error updating the workout."
        };

        var onUpdateFinally = function () {
            $scope.workouts = WorkoutService.query();
            $scope.isBusy = false;
            $scope.editing = false;
        };

        $scope.editWorkout = function (currentWorkout) {
            crudInit();
            $scope.workout = currentWorkout; //sets up the hidden UI element
            $scope.editing = true; //flag for ng-hide
        };

        /*callback for ng-click 'updateWorkout': */
        $scope.updateWorkout = function (newWorkout) {
            WorkoutService.update({id: newWorkout.id}, newWorkout)
                .$promise
                .then(onUpdateWorkoutComplete, onUpdateError)
                .finally(onUpdateFinally);
        };

        //DELETE
        var onDeleteWorkoutComplete = function (data) {
            $scope.successMessage = "Workout '" + $scope.workout.workout_name + "' has been deleted."
        };

        var onDeleteError = function (response) {
            $scope.errorMessage = "Error deleting the workout."
        };

        /*callback for ng-click 'deleteWorkout':
         Learning Note: the update to workouts must be declared in the finally block to ensure the consecutive http call is
         done AFTER the first one. If you put it outside there's no guarantee it will happen in the order you coded it!*/
        $scope.deleteWorkout = function (workout) {
            crudInit();
            $scope.workout = workout;

            WorkoutService.delete({id: $scope.workout.id})
                .$promise
                .then(onDeleteWorkoutComplete, onDeleteError)
                .finally(function () {
                    $scope.workouts = WorkoutsService.query();
                    $scope.isBusy = false;
                });
        };
    }]);

    app.controller('WorkoutCreationCtrl', ['$scope', 'WorkoutsService', 'UserService', function ($scope, WorkoutsService, UserService) {
        $scope.workout = {};
        $scope.exercises = [];
        $scope.newExercise = {};

        $scope.isBusy = false;
        $scope.successMessage = "";
        $scope.errorMessage = "";

        var crudInit = function () {
            $scope.isBusy = true;
            $scope.successMessage = "";
            $scope.errorMessage = "";
        };

        $scope.addExercise = function () {
            $scope.exercises.push($scope.newExercise);
            $scope.newExercise = {};
        };

        //CREATE
        var onCreateWorkoutComplete = function () {
            $scope.successMessage = "Workout created!";
        };

        var onCreateError = function () {
            $scope.errorMessage = "Failed to create the new workout.";
        };

        var onUserSuccess = function (data) {
            $scope.gotUser = true;
            $scope.user = data;
        };

        var onUserError = function () {
            $scope.gotUser = false;
        };

        var createWorkoutWithUser = function (currentUser) {
            $scope.workout.created_by = currentUser['0'].id;

            WorkoutsService.create($scope.workout)
                .$promise.then(onCreateWorkoutComplete, onCreateError)
                .finally(function () {
                    $scope.isBusy = false;
                    $scope.workout = {};
                    $scope.exercises = [];
                });
        };

        $scope.createWorkout = function (exercises) {
            crudInit();
            $scope.workout.exercises = exercises;

            var finished = false;
            UserService.query()
                .$promise.then(onUserSuccess, onUserError)
                .finally(function(){
                    if ($scope.gotUser){
                        createWorkoutWithUser($scope.user)
                    }else{
                        $scope.errorMessage = "You must sign in to create a workout";
                    }
                });

        };

    }]);

    app.controller('LoginCtrl', ['$scope', '$rootScope', '$location', 'AuthenticationService', function ($scope, $rootScope, $location, AuthenticationService) {
        $scope.busy = false;
        $scope.username = 'guest';
        $scope.password = 'abcpassword123';

        var loginInit = function () {
            $scope.busy = true;
        };

        $scope.login = function (username, password) {
            loginInit();

            AuthenticationService.Login(username, password, function (result) {
                if (result === true) {
                    $scope.busy = false;
                    $rootScope.isSignedIn = true;
                    $location.path('/');
                } else {
                    $scope.busy = false;
                    $scope.errorMessage = "username/password combination is incorrect";
                }
            });
        }

    }]);

}());