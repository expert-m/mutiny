var SubscribeCtrl = function ($scope, $rootScope) {
    $rootScope.leftBlock = false;
};

SubscribeCtrl.resolve = {};

app.controller('SubscribeCtrl', SubscribeCtrl);


var UnsubscribeCtrl = function ($scope, $rootScope) {
    $rootScope.leftBlock = false;
};

UnsubscribeCtrl.resolve = {};

app.controller('UnsubscribeCtrl', UnsubscribeCtrl);
