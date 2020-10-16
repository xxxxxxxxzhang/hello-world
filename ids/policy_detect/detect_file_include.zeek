##! File Upload attack detection.

@load base/protocols/http/main.zeek
@load base/protocols/http/utils.zeek
@load base/protocols/http

module HTTP;
export {
    ## Describes the type of notice we will generate with the Notice framework.
    ## Notices allow Zeek to generate some kind of extra notification beyond its default log types.
    redef enum Notice::Type += {
		    File_Include_Attack,
    };
	

}
event http_header(c: connection, is_orig: bool, name: string, value: string)
    {
        print( c$http$uri);   
        if (  "GET" in c$http$method&&  "/tmp/sess" in c$http$uri)
            {
   	          
          	   local n: Notice::Info = Notice::Info($note=File_Include_Attack, 
                                                 $msg="include file", 
                                                 $conn=c);
    
          	  print( c$http$uri);                                      
          	  NOTICE(n);
            }                 
    }
