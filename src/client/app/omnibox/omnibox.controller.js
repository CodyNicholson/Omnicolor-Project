(function() {
    'use strict';

    angular.module('app.omnibox').controller('OmniboxController', ['$scope', '$http', function($scope, $http) {
        var vm = this;
        vm.colorSelection = 'Wine';
        vm.bgColor = {'red': 0, 'green': 0, 'blue': 0}; //default
        vm.colors = [];

        $http.get('http://localhost:5000/all')
            .then(function(res) {
                // console.log(res.data);
                vm.colors = res.data
            });

        $scope.$watch('oc.searchText', function(newVal, oldVal) {
            console.log('newVal: ' + newVal + ' | oldVal: ' + oldVal);
            return $http
                .get('http://localhost:5000/' + vm.searchText)
                .then(function(res) {
                    console.log(res.data);
                    vm.bgColor = res.data;
                });
        }, true);

        vm.getColor = function() {
            return {'background-color': 'rgb(' + vm.bgColor.red + ', ' + vm.bgColor.green + ', ' + vm.bgColor.blue + ')'};
        }
    }]);

})();
