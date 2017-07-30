(function() {
    'use strict';

    angular.module('app.omnibox').filter('capitalize', function() {
        return function(input) {
            if(!!input) {
                if(input.includes(' ')) {
                    input = input.split(' ');

                    for(var i = 0; i < input.length; i++) {
                        input[i] = input[i].charAt(0).toUpperCase() + input[i].substr(1).toLowerCase();
                    }

                    return input.join(' ');
                } else {
                    return input.charAt(0).toUpperCase() + input.substr(1).toLowerCase();
                }
            }

            return '';
        }
    });
})();
