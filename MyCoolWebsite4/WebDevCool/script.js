var myApp = angular.module('myApp',[]);

myApp.controller('MyCtrl', [ '$scope', function($scope){
  $scope.foo = 'Some default value';
}]);