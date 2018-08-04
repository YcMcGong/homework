BH.add('StylingService', function() {
	
	"use strict";
    eval(BH.System);

    var StylingService = BH.Class(BH.Widget, {

		// Stub
        save_user_info: function(data, successCb, errorCb) {
		
			var random = Math.floor(Math.random() * (2));
			
			if (random === 0) {
				if (successCb) {
					successCb({
						// BUT NO.4 added first_name and kept the random error
						// 'scheduled_appointment_date': 1543000626
						'scheduled_appointment_date': '11/23/2018 11:17 am PST',
						'first_name': data.first_name,
					});
				}
			} else {
				if (errorCb) {
					errorCb('Sorry, something went wrong.');
				}
			}			
        }

    });

    if (!BH.StylingService) {
        BH.StylingService = new StylingService();
        BH.StylingService.render();
    }
});
