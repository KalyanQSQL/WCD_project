-- this macro returns the description of the channel type

{% macro generate_channel_type(channel_key) %}

    case{{channel_key}}
        when 1 then 'Catalog'
        when 2 then 'Web'
    end 

{% endmacro %}