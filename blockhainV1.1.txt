pragma solidity 0.7.0;

contract OptStore{

    struct Provider {
        address adrProv;
        uint id;
        string nameFirmSell;
        string addressFirmSell;
        string phoneNumberSell;
    }

    struct Buyer {
        address adrBuyer;
        uint id;
        string nameFirmBuy;
        string addressFirmBuy;
        string phoneNumberBuy;
    }

    struct Good{
        uint id;
        string nameFirm;
        string nameGoods;
        string units;
        uint amount;
        uint valueBuy;
        uint valueSell;
    }

    struct makeDeal{
        string idBuyer;
        string idSeller;
        uint id;
        uint amountSellGoods;
    }

    mapping(uint => Provider) public providers;
    mapping(uint => Good) public goods;
    mapping(uint => Buyer) public buyers;

    makeDeal[] deals;

    uint num_goods =0;
    address public admin;
    constructor() public {
        admin = msg.sender;
    }

    modifier OnlyAdmin{
        require(msg.sender == admin, "Not Admin");
        _;
    }

    function get_deal_num() public view returns(uint){
        return deals.length - 1;
    }

    function get_goods_num() public view returns(uint){
        return num_goods;
    }

    // Добавление провайдера (добавляется по уникальному номеру товара)
    function add_Provider(uint _idGood ,uint _id, string memory _nameFirm, string memory _addressFirm, string memory _phoneNumber, address owner_provider) public OnlyAdmin{
        require(owner_provider != address(0), "Wrong address");
        require(providers[_idGood].adrProv == address(0), "Id has been already used");
        providers[_idGood] = Provider(owner_provider,_id, _nameFirm, _addressFirm, _phoneNumber);
    }

    // Добавление покупателя (добавляются следом)
    function add_Buyer(uint _id, string memory _nameFirmBuy, string memory _addressFirmBuy, string memory _phoneNumberBuy,address owner_buyer ) public OnlyAdmin{
        require(owner_buyer != address(0), "Wrong address");
        require(buyers[_id].adrBuyer == address(0), "Id has been already used");
        buyers[_id] = Buyer(owner_buyer,_id, _nameFirmBuy, _addressFirmBuy,_phoneNumberBuy);
    }

    // Добавление товара (добавляются один за другим, имеют свой id, нужный для поиска
    // поставщика по этому id)
    function add_Good(uint _idGood, string memory _nameFirm, string memory _nameGoods, string memory _units, uint _amount, uint _valueBuy, uint _valueSell) public OnlyAdmin {
        goods[num_goods] = Good(_idGood, _nameFirm, _nameGoods, _units, _amount, _valueBuy, _valueSell);
        num_goods+=1;
    }

    function add_amount_of_good(uint _id, uint _amountGood) public {
        goods[_id].amount += _amountGood;
    }

    function remove_amount_of_good(uint _id, uint _removeGood) public {
        goods[_id].amount -= _removeGood;
    }

    function add_deals(uint _id, uint _amountSellGoods, string memory _idBuyer, string memory _idSeller) public OnlyAdmin {
        deals.push(makeDeal(_idBuyer, _idSeller, goods[_id].id, _amountSellGoods));
    }
    // Покупка товара фирмой
    function buy_good(uint _id, uint _removeGood, address toShop) public payable {
        require(goods[_id].amount >= _removeGood, "Goods are not enough");
        require(msg.value == goods[_id].valueSell*_removeGood , "Wrong amount of miney");
        remove_amount_of_good(_id, _removeGood);
        payable(toShop).transfer(msg.value);
    }

}