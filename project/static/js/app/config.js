app.config(function ($httpProvider, $interpolateProvider, $locationProvider, $routeProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    $locationProvider.html5Mode(true);

    $routeProvider.when('/404/', {
        templateUrl: '/static/html/404.html',
        controller: '404Ctrl'
    });

    $routeProvider.otherwise({
        redirectTo: '/404/'
    });
});

app.config(function ($qProvider) {
    $qProvider.errorOnUnhandledRejections(false);
});

app.config(function (ngProgressLiteProvider) {
    ngProgressLiteProvider.settings.trickleSpeed = 100;
});
