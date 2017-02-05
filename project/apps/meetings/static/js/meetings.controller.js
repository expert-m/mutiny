var ListMeetingsCtrl = function ($scope, meetings) {
    $scope.meetings = meetings.results;
};

ListMeetingsCtrl.resolve = {
    meetings: function (api) {
        return api('meetings').getPage(0, 50);
    }
};

app.controller('ListMeetingsCtrl', ListMeetingsCtrl);
